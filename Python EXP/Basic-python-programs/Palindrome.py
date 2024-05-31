def ispalindrome(s):
  s = s.lower()
  return s == s[::-1]

s = input("Enter a string: ")
print(ispalindrome(s))
