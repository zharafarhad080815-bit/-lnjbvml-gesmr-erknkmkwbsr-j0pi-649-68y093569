#Write a Python class to reverse a string word by word.
class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

# Example usage
reverser = StringReverser("Hello World")
print(reverser.reverse_words())  # Output: "World Hello"