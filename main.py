def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = word_counter(text)
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

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars        
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