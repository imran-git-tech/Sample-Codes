# Simple word count program

def count_words(text):
    # Split the text into words based on spaces
    words = text.split()
    return len(words)

# Example usage
user_input = input("Enter a sentence or paragraph: ")
word_count = count_words(user_input)
print(f"Word count: {word_count}")

