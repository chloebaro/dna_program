def is_palindrome(word):
    """ (str) -> bool
    
    Precondition: used only for strings that consist only of lowercase 
    alphabetic characters.
    
    Return True iff word is a palindrome. 
    
    Examples:
    >>> is_palindrome("radar")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("goodbye")
    False
    >>> is_palindrome("a")
    True
    >>> is_palindrome("")
    True
    
    """
    
    reverse_word = ""
    index = len(word) - 1 
    """we will start adding characters in reverse_word starting from the last 
    character in word"""
    
    while(index > -1):
        reverse_word = reverse_word + word[index] 
        index = index - 1
        """ adds the characters from word to reverse_word starting from the last 
        character in word and ending at the first character in word."""
    
    return word == reverse_word

def is_palindromic_phrase(phrase):
    """ (str) -> bool
    
    Return True iff phrase is a palindrome (disregarding non-alphabetic 
    characters and treating uppercase letters and lowercase letters as the
    same).
    
    Examples:
    >>> is_palindromic_phrase("radar")
    True
    >>> is_palindromic_phrase("Radar")
    True
    >>> is_palindromic_phrase("Ra d Ar")
    True
    >>> is_palindromic_phrase("rad?ar")
    True
    >>> is_palindromic_phrase("radar9")
    True
    >>> is_palindromic_phrase("radart")
    False
    >>> is_palindromic_phrase("12321")
    True
    
    """
    
    index = 0
    
    """In the following while loop I remove non-alphabetic characters from 
    phrase and assign the result to new_phrase."""
    
    new_phrase = phrase
    while index < len(new_phrase):
        if not(new_phrase[index].isalpha()):
            if(new_phrase[index] == len(new_phrase) - 1):
                new_phrase = new_phrase[:index]
                index = index - 1
            else:    
                new_phrase = new_phrase[:index] + new_phrase[index + 1:]
                index = index - 1
        index = index + 1        
        
    new_phrase = new_phrase.lower() 
    """ I added the above code because we treat uppercase and lowercase letters
    in the same way."""
    
    
    return is_palindrome(new_phrase)
    
def get_odd_palindrome_at(word, center_index):
    """ (str, int) -> str
    
    Precondition: All the characters in word are lowercase alphabetical 
    characters. center_index must be in the bounds of word.
    
    Return the longest palindrome that has an odd length whose center is 
    at center_index in the word string.
    
    Examples: 
    >>> get_odd_palindrome_at("oradarp", 3)
    'radar'
    >>> get_odd_palindrome_at("pada", 2)
    'ada'
    >>> get_odd_palindrome_at("acca", 2)
    'c'
    
    """

    forward_index = center_index + 1
    backward_index = center_index - 1
    palindromes = []
    longest_palindrome = ""
    
    
    """ The following loop checks to see whether each odd-length sequence of 
    characters whose center is at center_index is a palidrome. If it is a 
    palindrome, it is added to the palindromes list. """
    while((forward_index < len(word)) and (backward_index > -1)):

        if is_palindrome(word[backward_index:forward_index + 1]):
            palindromes.append(word[backward_index:forward_index + 1])
            
        forward_index += 1
        backward_index -= 1
        
    if len(palindromes) == 1: 
        """ If we've only added one palindrome to the list then it is by default
        the biggest palindrome in the string."""
        return palindromes[0]
    elif len(palindromes) == 0:
        """We must also evaluate the case where there have been no palindromes 
        added the list. However, we could single alphabetic characters as 
        palindromes, thus we can return the character at the center_index as 
        the largest palindrome in the string."""
        return word[center_index]
    else:
        for p in range(1, len(palindromes)):
            longest_palindrome = max(palindromes[p], palindromes[p - 1])
    return longest_palindrome
                               
    