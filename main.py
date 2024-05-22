
def num_words(string):
    words = string.split()
    return len(words)


def num_letters(string):
    lower = string.lower()
    dict_count = {}

    letters = [*lower]

    for i in letters:
        if ord(i) >= 97 and ord(i) <= 122:
            if i in dict_count:
                dict_count[i] += 1
            else:
                dict_count[i] = 1
    
    return dict_count


def get_num(string):
    return int(string.split()[-2])


def make_report(wordCount, letterCount):
    report = f"--- Begin report of books/frankenstein.txt ---\
        \n{wordCount} words found in the document\n"

    lst = []
    for key, val in letterCount.items():
        lst.append(f"\nThe '{key}' character was found {val} times")
        #report += f"\nThe '{key}' character was found {val} times"
    
    ordered = sorted(lst, reverse=True, key=get_num)

    for i in ordered:
        report += i

    report += "\n--- End report ---"
    return report


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = num_words(file_contents)
    letter_dict = num_letters(file_contents)

    print(make_report(word_count, letter_dict))
    
main()
