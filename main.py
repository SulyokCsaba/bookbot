def main():
    with open("books/frankeinstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
    
main()

def count_words():
    with open("books/frankeinstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
    word_count= 0
    for word in words:
        word_count += 1
    print(f"{word_count} words found in the document\n")

count_words()

def count_each_letters():
    letter_counter = {}
    with open("books/frankeinstein.txt") as f:
        raw_file_contents = f.read()
        file_contents=raw_file_contents.lower()
        words = file_contents.split()
    a = []
    for word in words:
        for char in word:
            a.append(char)
    for i in a:
        if i.isalpha():
            letter_counter[i] = 0
    for i in a:
        if i.isalpha():
            letter_counter[i] += 1
    letter_counter_sorted = sorted(letter_counter, key=letter_counter.get, reverse=True)
    for r in letter_counter_sorted:
        print(f"The '{r}' character was found {letter_counter[r]} times")
count_each_letters()

print("--- End report ---")




        
