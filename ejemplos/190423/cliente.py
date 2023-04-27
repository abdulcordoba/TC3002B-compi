from antlr4 import *
from antlr.SimpleLexer import SimpleLexer;
from antlr.SimpleParser import SimpleParser;
from antlr.SimpleListener import SimpleListener;

INTEGER=0
FLOAT=1
STRING=2

class Declarator(SimpleListener):
    def __init__(self):
        self.symbol_table = {}

    def enterInt_decl(self, ctx:SimpleParser.Int_declContext):
        # Validar si la variable ya existe -> excepción

        self.symbol_table[ctx.VARIABLE().getText()] = INTEGER
        # Completar con las demás declaraciones

class TypeChecker(SimpleListener):
    def __init__(self, table):
        self.symbol_table = table

    def exitInteger(self, ctx:SimpleParser.IntegerContext):
        ctx.type = INTEGER

    def exitVariable(self, ctx:SimpleParser.VariableContext):
        ctx.type = self.symbol_table[ctx.VARIABLE().getText()]

    def exitRoot(self, ctx:SimpleParser.RootContext):
        if ctx.expr(0).type == STRING or ctx.expr(1).type == STRING:
            raise Exception("Operando incorrecto para raíz")

        ctx.type = FLOAT

    def exitAssign(self, ctx:SimpleParser.AssignContext):
        if self.symbol_table[ctx.VARIABLE().getText()] != ctx.expr().type:
            raise Exception("Asignación de tipos incorrectos")

def main(argv):
    input = FileStream(argv)
    lexer = SimpleLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SimpleParser(stream)
    tree = parser.programa()

    walker = ParseTreeWalker()

    #declarator = Declarator()
    #walker.walk(declarator, tree)

    #typechecker = TypeChecker(declarator.symbol_table)
    #walker.walk(typechecker, tree)

if __name__ == '__main__':
    main("ejemplo3.txt")
