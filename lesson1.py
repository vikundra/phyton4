def isPalindrome (s):
    reva=""
    for let in reversed(s):
        reva=reva+let
    return reva==s

def isPalindrome2(s): 
    return s[::-1] == s 


a = input('Введите фразу:')
print(isPalindrome(a))
print(isPalindrome2(a))
