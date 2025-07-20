# takes a str and returns number of words as int

def get_num_words(text):
    num_words = len(text.split())
    return num_words



# takes a str and returns a dictionary with the char and number of of it (including spaces and symbols)

def char_in_text(text):
    dict_text = {}
    text_lower = text.lower()
    for char in text_lower:
        if char in dict_text:
            dict_text[char] += 1
        else:
            dict_text[char] = 1
    return dict_text



# takes a dict with its key-value pairs {"a":32498} and returns a list w/ two dicts [{"char": "a",}, {"num": 32498}]
def sort_chars_by_num(dict):
    sorted_chars = []
    for char, count in dict.items(): # mit .items() kann char und count befüllt werden
        if char.isalpha() is True: # prüfung ob char ein alphabetischer ist
            char_num_dict = {
                "char": char,
                "num": count
            }
            sorted_chars.append(char_num_dict)
    
    # returns key "num"
    def sort_on(items):
        return items["num"]

    sorted_chars.sort(reverse=True, key=sort_on)
  
    return sorted_chars





