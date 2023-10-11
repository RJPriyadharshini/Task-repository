# 3 write a function that takes a string and returns the number a new string with all the vowels removed
def remove_vowels(string):
  vowels = set("aeiou")          # set vowels
  new_string = ""                # create empty string
  for char in string:            # char == string
    if char not in vowels:       # prydhrshn
      new_string += char         # Add the char which are not presented in vowels
  return new_string

print(remove_vowels("priyadharshini"))


#4    write a function that takes a string and returns the number of unique characters in it


def count_unique_characters(string):
  unique_characters = set()            # empty set created because set does not allow duplicate values
  for character in string:             # character == string
    unique_characters.add(character)    # add characters
  return len(unique_characters)
print(count_unique_characters("priyadharshini"))


#5  write a function that takes a string and returns true if it is pallindrome  , false otherwise
def is_palindrome(string):
  string = string.lower().replace(" ", "")    # convert the string as lower case and remove gaps
  reversed_string = string[::-1]           # reverse ,it returns the value from backwards
  return string == reversed_string

print(is_palindrome("madam"))


#6
def longest_common_substring(str1, str2):
    max_length = 0
    start_index = 0
    for i in range(len(str1)):      # 14
        for j in range(len(str2)):   # 8
            length = 0
            while i + length < len(str1) and j + length < len(str2) and str1[i + length] == str2[j + length]:    # 14<14 and 8<8  and  str1[14]==str2[8]
                length += 1
            if length > max_length:
                max_length = length
                start_index = i
    longest_substring = str1[start_index:start_index + max_length]
    return longest_substring

str1 = "abcdef"
str2 = "bcdfg"
result = longest_common_substring(str1, str2)
print("Longest common substring:", result)

print(longest_common_substring("priyadharshini","pradeepa"))



# 7 write a function that takes a string and returns most frequent charcter in it
def most_frequent_character(string):
  character_counts = {}          # create empty dict
  for character in string:
    if character in character_counts:
      character_counts[character] += 1      # if same char repeated add the count
    else:
      character_counts[character] = 1       # if not repeated take the count as 1
  most_frequent_character = max(character_counts, key=character_counts.get)    # by using max function it fetch max count from the string by using the key only it correctly fetch the max count

  return most_frequent_character

print(most_frequent_character("geeksforgeeks"))

# 8

# anagram means we take one word like heart then change that as Earth .. It is anagram. by taking one meaningful word and change that to other meaningful word
def is_anagram(str1, str2):
  str1 = str1.lower()
  str2 = str2.lower()
  str1 = sorted(str1)       # sorted used to order in alphabetical order to easily identify whether it is anagram or not
  str2 = sorted(str2)
  return str1 == str2

print(is_anagram("listen","silent"))

#9  write a function that takes a string and returns number of word in it

def count_words(string):
  words = string.split()  # by using split for eg "hello world" it returns 1 can changed as "hello" "world" it returns 2
  return len(words)
print(count_words("pavithra"))
print(count_words("priya dharshini"))


""" TASK - 2"""

#1
list1 = [10, 501, 22, 37, 100, 999, 87, 351]
even_list = []
odd_list = []

for num in list1:
  if num % 2 == 0:
    even_list.append(num)
  else:
    odd_list.append(num)

print("Even list:", even_list)
print("Odd list:", odd_list)

# 2

def is_prime(n):
  if n <= 1:           # 0 then negative values not included in prime
    return False
  for i in range(2, int(n**0.5) + 1):         # n**0.5 to take the square root (2,3.1+1)=(2,4)
    if n % i == 0:          #10/3!=0  so 10 is not prime
      return False
  return True

list1 = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = [num for num in list1 if is_prime(num)]

print(prime_numbers)


#3
"""“happy” is a number which sum of its squared digits will eventually be 1, after infinite number of iterations"""

def is_happy_number(n):
  seen = set()
  while n != 1 and n not in seen:          #This loop continues until either n becomes 1
    seen.add(n)         # it take only non happy numbers
    sum_of_squares = 0
    while n > 0:
      remainder = n % 10
      sum_of_squares = sum_of_squares + remainder * remainder
      n //= 10
    n = sum_of_squares
  return n == 1

list1 = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = sum(is_happy_number(num) for num in list1)
print(happy_numbers)

#4

def sum_first_last_digit(number):
    num_str = str(number)
    first_digit = int(num_str[0])          # take 1st num
    last_digit = int(num_str[-1])          # take last num
    sum_digits = first_digit + last_digit   # add both 1st and last
    return sum_digits
number = int(input("Enter an integer: "))  # Input the integer
result = sum_first_last_digit(number)  # Calculate the sum of first and last digits
print("Sum of first and last digit:", result)  # Print the result


#5

def distribute_mangoes(mangoes, students):
  mangoes.sort(reverse=True)
  student_mangoes = [0] * students
  for i in range(len(mangoes)):
    student_mangoes[i % students] += mangoes[i]
  return max(student_mangoes) - min(student_mangoes)
mangoes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
students = 5

difference = distribute_mangoes(mangoes, students)

print(difference)


#6

def merge_lists(list1, list2, list3):
    merged_list = list1 + list2 + list3
    unique_elements = list(set(merged_list))      # set not allow duplicates
    return unique_elements

result = merge_lists([1, 2, 3], [3, 4, 5], [5, 6, 7, 8])
print(result)

#7

def first_non_repeating_number(list1):
  seen = set()
  for number in list1:
    if number not in seen:
      return number
    seen.add(number)
  return -1

list1 = [1, 2, 3, 4, 5, 1, 2, 3]
first_non_repeating_number = first_non_repeating_number(list1)
print(first_non_repeating_number)
