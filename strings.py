#!/usr/bin/env python3.8

"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
#import pytest

## Question 1
def no_duplicates(a_string):
    a_string = sorted(a_string)
    dup = ""
    for char in a_string:
        if char not in dup:
            dup = dup + char
    print(dup)
    pass

## Question 2
def reversed_words(a_string):
    list_words = a_string.split()
    print(list_words[::-1])
    pass

## Question 3
def four_char_strings(a_string):
    split_string = []
    n = 4
    for index in range(0, len(a_string), n):
        split_string.append(a_string[index : index + n])
    print(split_string)
    pass


def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


#def main():
#    return pytest.main(__file__)


#if __name__ == '__main__':
#    main()
    
