#Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer.
# NOTE: One or two additional variables are fine. An extra copy of the array is not.
#FOLLOW UP
#Write the test cases for this method.
import math

length = 0
#PRE: non-empty string
#POST: string with all duplicates removed
def removeDup(str):
    str_list = list(str)
    global length
    length = len(str_list)
    str_list = heapify(str_list) #min heap
    prev = extract_min(str_list)
    for i in range(0,length):
        curr = extract_min(str_list)
        if curr == prev:
            #pop the prev, which is located at last index of heap + 1
            str_list.pop(length)
        prev = curr
    return str_list

def heapify(str_list):
    # global length
    # length = len(str_list)
    start_index = math.floor(len(str_list)/2)-1
    for i in range(start_index, -1, -1):
        str_list = trickleDown(i, str_list)
    return str_list

def trickleDown(i, list):
    while i < length:
        left = (i+1)*2 -1
        right = (i+1)*2
        if left < length:
            smallerChildIndex = left
            if right < length and list[right] < list[left]:
                smallerChildIndex = right
            #swap if parent is bigger than child
            if list[i] > list[smallerChildIndex]:
                list[i], list[smallerChildIndex] = list[smallerChildIndex], list[i]
            i = smallerChildIndex
        else:
            break
    return list


def extract_min(str_list):
    global length
    char = str_list[0]
    str_list[0], str_list[length-1] = str_list[length-1], str_list[0]
    length-=1
    trickleDown(0, str_list)
    return char

# str = "btiornvfewa"
# str_l = list(str)
# print(heapify(str_l))

#test cases:
print(removeDup("a"))
print(removeDup("aa"))
print(removeDup("abba"))
print(removeDup("fedcbafd"))
print(removeDup("fdssafdsfsaasdfdsasadfdfsafdsfdfsfdsafdsa"))