def count_words(string):
    wordlist = string.split()
    return len(wordlist)

def count_characters(string):
    string = string.lower()
    character_count = {}
    for character in string:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def sort_on(dictionary):
    return dictionary["character_count"]

def sort_dictionary(dictionary):
    sorted_list = []
    for key in dictionary:
        sorted_list.append({"character": key, "character_count": dictionary[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
