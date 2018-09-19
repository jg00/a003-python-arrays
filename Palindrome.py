word = input("Enter a word: ")

last_letter_index = len(word) - 1
flag = False

for index in range(0, len(word),1):
    if (word[index] != word[last_letter_index]):
        break
    else:
        last_letter_index = last_letter_index - 1
        flag = True

print("Is {} a Palindrome? {}".format(word,flag))


# reference
# for index in range(0, len(word),1):
#     print(word[index])
#     # print(index)
#     # print(len(word)-1)
#     last_letter_index = last_letter_index -1
#     # print(last_letter_index)
#     print(word[last_letter_index])


# range(start, stop, step)
# start: Starting number of the sequence.
# stop: Generate numbers up to, but not including this number.
# step: Difference between each number in the sequence.


