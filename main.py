import sys

def count_words(string):
    word_count = len(string.split())
    print(f"file has {word_count} words")

def get_file_content(path):
    with open(path) as f:
        return f.read()

def character_times(text):
    text = text.lower()
    dict = {}
    for character in text:
        if character in dict.keys():
            dict[character] += 1
        else:
            if character.isalpha():
                dict[character] = 1
    for key in sorted(dict.keys()):
        print(f"'{key}' appears {dict[key]} times")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        return 1

    path = sys.argv[1]
    try:
        print(f"--- Begin report of {path} ---")
        text = get_file_content(path)
        count_words(text)
        character_times(text)
        print("--- End report ---")
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return 1
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 1

    return 0

main()

