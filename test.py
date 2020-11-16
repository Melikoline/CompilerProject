#****** CONSTANTS ******
DIGITS = "0123456789"

#****** Errors ******
class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f"{self.error_name}: {self.details}"
        return result
#******* Variable *******
TT_INT = "Sahih"            # int
TT_FLOAT = "Ashari"         # float
TT_CHAR = "Harf"            # char

#****** Operators ******
TT_PLUS = "Jam"             # +
TT_PLUS_ONE = "YekiBala"    # ++
TT_MINUS = "Kam"            # -
TT_MINUS_ONE = "YekiPain"   # --
TT_MUL = "Zarb"             # *
TT_DIV = "Tagsim"           # /
TT_LEFT_OVER = "Bagimonde"  # %

#****** Logical operators ******
TT_BIGGER = "&B"            # >
TT_LARGER_EQUALS = "&BM"    # >=
TT_SMALLER = "&K"           # <
TT_SMALLER_EQUALS = "&KM"   # <=
TT_EQUAL = "&MM"            # ==
TT_LPAREN = "Lparen"        # (
TT_RPAREN = "RPAREN"        # )

#****** TOKEN ******
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value : return f"{self.type}:{self.value}"
        return f"{self.type}"

#****** LEXER ******
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1 
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in " \t":
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == "+":
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == "-":
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == "*":
                tokens.append(Token[TT_MUL])
                self.advance()
            elif self.current_char == "/":
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == "(":
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                #Result Some Error
        return tokens

        def make_number(self):
            num_str = ''
            dot_count = 0

            while self.current_char != None and self.current_char in DIGITS + ".":
                if self.current_char == ".":
                    if dot_count == 1 : break
                    dot_count += 1
                    num_str += "."
                else:
                    num_str += self.current_char

            if dot_count == 0:
                return Token(TT_INT, int(num_str))
            else:
                return Token(TT_FLOAT, float(num_str))  
