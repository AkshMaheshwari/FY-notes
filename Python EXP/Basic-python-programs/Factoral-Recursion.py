def factorial(n):
  if(n==1):
    return 1

  else:
    return n*factorial(n-1)

n = int(input("Enter a number: "))
print(f"factoral of {n} is:",factorial(n))
