def count_words(text):
    # counts how many words are in the text string
    words = text.split()    # split text into a list of words
    return len(words)       # count how many words are in the list

def count_characters(text):
    # counts the number of times each char appears in the text
    text = text.lower()     # convert entire text to lowercase
    char_count = {}         # create empty dictionary to store counts

    for char in text:               # loop to count each char
        if char in char_count:      # if character in character counts
            char_count[char] += 1   # increment count if char already exists
        else:           
            char_count[char] = 1    # start new count at 1 if new character

    return char_count               # return the filled dictionary with counts
    
def sort_char(item):
    # helper function, to return the num key of each dictionary for comparison
    return item["num"]
    # comment everything out
def sort_character_counts(char_counts):
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=sort_char)
    # print(char_list) out for a sec

    return char_list
