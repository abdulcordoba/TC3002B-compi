grammar Simple;

programa : sentencia+;

sentencia :
    'if' expr 'then' sentencia+ 'fi'                #if
    | 'while' expr 'do' sentencia+ 'wend'           #while
    | 'definition' type VARIABLE '(' ')' sentencia+ 'end'  #func
    | declaration                                   #decl
    | VARIABLE '<-' expr                            #assign
    | 'return' expr                                 #return
    ;

type :
    'int' | 'float' | 'string';

declaration:
    'int' VARIABLE        #int_decl
    | 'float' VARIABLE    #float_decl
    | 'string' VARIABLE   #str_decl
    ;

expr :
    expr '^' expr      #raise
    | expr '_' expr    #root
    | expr '*' expr    #mult
    | expr '/' expr    #div
    | expr '+' expr    #add
    | expr '-' expr    #sub
    | VARIABLE '(' ')' #call
    | '(' expr ')'     #parents
    | INT_L            #integer
    | FLOAT_L          #float
    | STR_L            #string
    | VARIABLE         #variable
    ;





// Lexer

// keywords

// symbols
VARIABLE  : [a-zA-Z]+ ;

// Literales
INT_L : [0-9]+;
FLOAT_L : [0-9]+ '.' [0-9]+ ;
STR_L : '"' [a-zA-Z]* '"' ;

NEWLINE : [\r\n]+ -> skip;
WS : [ ]+ -> skip;