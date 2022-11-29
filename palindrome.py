#! usr/bin/env python
"""
    author: Marcelo F. Gonzales
    description: Simple script to check if string is a palindrome or not
"""

def is_palindrome(word : str) -> bool:
    """palindrome function that checks recursively if the word is a palindrome or not"""
    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

if __name__ == "__main__":
    result = is_palindrome(input())
    if result:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")
