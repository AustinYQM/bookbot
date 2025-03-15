def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()

def get_num_words(path):
    return len(get_book_text(path).split())

def char_count(path):
    book = get_book_text(path).lower()
    chars = {}
    for c in book:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_chars(chars):
    return {key: val for key, val in sorted(chars.items(), key=lambda ele: ele[1], reverse=True)}
