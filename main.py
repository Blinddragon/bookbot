def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = word_counter(text)
    #all_lower = convert_to_lower(text) #part of my solution for letter counter
    #letter_count = single_counter(all_lower) #part of my solution for letter counter
    chars_dict = get_chars_dict(text)
    report = report_func(chars_dict)
    complete_report = full_report(report)
    #print(complete_report)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the book")
    print()

    for item in complete_report:
        if not item["character"].isalpha():
            continue
        print(f"The {item["character"]} character was found {item["count"]} times")

    print("--- End report ---")


#my solution for single letter counter (only viable for specific characters):
#def single_counter(all_lower):
    #count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    #for letter in all_lower:
        #if letter in count:
            #count[letter] += 1
    #return count

#recommended solution for single letter counter:
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars        

#part of my solution for single letter counter:
#def convert_to_lower(text):
    #lower = text.lower()
    #return lower

def word_counter(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def report_func(chars_dict):
    list_of_chars = []
    for key, value in chars_dict.items():
        single_dict = {"character": key, "count": value}
        list_of_chars.append(single_dict)
    return list_of_chars

def full_report(report):
    sorted_list = sorted(report, key = lambda x: x["count"], reverse = True)
    return sorted_list



main()



#create list with different dicts in in, which look like this. {"character": "a", count: 1}
#return the character value and count value in a sentence