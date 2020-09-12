"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num %2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
    result = []

    # for item, i in enumerate(items):
    #     if i % 2 != 0:
    #         result.append(i)

    # for item in items:
    #     if items[item] % 2 != 0:
    #         result.append(item)

    for i in range(0,len(items)):
        if i % 2 != 0:
            result.append(items[i])
    
    return result


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f'{i}. {item}')

        i += 1


def get_range(start, stop):
    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in ['a','e','i','o','u']:
            chars.append('*')
        else:
            chars.append(letter)

    return "".join(chars)


def snake_to_camel(string):
    camel_case = []

    for word in string.split("_"):
        camel_case.append(word.title())
    
    return "".join(camel_case)

def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
        
    return longest


def truncate(string):
    result = []

    for char in string:
        if (len(result) == 0) or char != result[len(result)-1]:
            result.append(char)

    return "".join(result)

def has_balanced_parens(string):
    parens = 0

    for letter in string:
        if letter == '(':
            parens += 1
        elif letter == ')':
            parens -= 1

            # if parens < 0:
            #     return False

    return parens == 0


def compress(string):
    pass  # TODO: replace this line with your code
