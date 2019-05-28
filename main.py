from lexer import Lexer
from parser import Parser
from codegen import CodeGen

#text_input = """
#mostrarenpantalla(4 suma 4 resta 2);
#"""

#lexer = Lexer().get_lexer()
#tokens = lexer.lex(text_input)

#for token in tokens:
#	print(token)

#tokens = lexer.lex(text_input)

#pg = Parser()
#pg.parse()
#parser = pg.get_parser()
#parser.parse(tokens).eval()

fname = "input.toy"
with open(fname) as f:
	text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir("output.ll")