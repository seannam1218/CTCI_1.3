#Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer.
# NOTE: One or two additional variables are fine. An extra copy of the array is not.
#FOLLOW UP
#Write the test cases for this method.

#doesn't work because length changes in the middle of the loop, which doesn't update the loop range, resulting in index error
def removeDup(str):
    str_list = list(str)
    length = len(str_list)
    for i in range(0,length):
        for j in range(i+1, length):
            if str_list[i] == str_list[j]:
                str_list.pop(j)
                length -= 1
    return "".join(str_list)

'''
def removeDup(str):
    str_list = list(str)
    l = len(str)
    pos = 0
    return "".join(remove(str, l, pos))

def remove(str_list, l, pos):
    for j in range(pos+1, l - 1):
         if str_list[pos] == str_list[j]:
             str_list.pop(j)
             l -= 1
             pos += 1
    if l > 0 and pos < l:
        return remove(str_list, l, pos)
'''
print(removeDup("sabcdsefgs"))