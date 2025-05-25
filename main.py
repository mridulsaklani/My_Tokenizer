book = {
    "a": 1,
    "b": 2,
    "c": 4,
    "d": 5,
    "e": 6,
    "f": 7,
    "g": 8,
    "h": 9,
    "i": 10,
    "j": 11,
    "k": 12,
    "l": 13,
    "m": 14,
    "n": 15,
    "o": 16,
    "p": 17,
    "q": 18,
    "r": 19,
    "s": 20,
    "t": 21,
    "u": 22,
    "v": 23,
    "w": 24,
    "x": 25,
    "y": 26,
    "z": 27,
    "A": 28,
    "B": 29,
    "C": 3,   
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
    "0": 53,
    "1": 54,
    "2": 55,
    "3": 56,
    "4": 57,
    "5": 58,
    "6": 59,
    "7": 60,
    "8": 61,
    "9": 62,
    " ": 63,
    ".": 64,
    ",": 65,
    "!": 66,
    "?": 67,
    "'": 68,
    "\"": 69,
    ":": 70,
    ";": 71,
    "-": 72,
    "_": 73,
    "(": 74,
    ")": 75,
    "[": 76,
    "]": 77,
    "{": 78,
    "}": 79,
    "\n": 80,
    "\t": 81,
    " ": "xxx"
}


text = "My name is Mridul singh saklani Rajput"

text_tokens = [39, 26, 'xxx', 21, 9, 10, 19, 5, 'xxx', 13, 6, 8, 'xxx', 20, 10, 27, 6, 'xxx', 10, 20, 'xxx', 59, 64, 58, 'xxx', 10, 15, 4, 9, 'xxx', 2, 22, 21, 'xxx', 35, 'xxx', 1, 14, 'xxx', 20, 21, 10, 13, 13, 'xxx', 23, 10, 19, 8, 10, 15]

token = []

def get_token(book: dict):
    for i in text:
       token_value =  book.get(i)
       token.append(token_value)

get_token(book)
print(token)

message = []

def parse_token(book:dict):
        for i in text_tokens:
            for k, v in book.items():
              if v == i:
                message.append(k)
      
parse_token(book)


main_msg = "".join(message)
print(main_msg)

