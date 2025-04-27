def get_num_words(text):
    return len(text.split())


def get_char_counts(text):
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


def get_sorted_char_counts(char_counts):
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list 