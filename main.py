"""This program counts the number of vowels in a string."""

def count_vowels(string:str) -> int:
    """
    Takes in a string and returns the number of vowels in the string.

    Args:
        string (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
    vogais = "aeiouAEIOU"  

    cont = 0  
    for ca in string:
        if ca in vogais:  
            cont += 1  

    return cont