'''
🧾 The Code:
python
Copy
Edit
n = int(input())
result = ''.join(map(str, range(1, n + 1)))
print(result)
🧠 Explanation:
1. n = int(input())
This line takes user input (which is a string), converts it to an integer, and stores it in the variable n.

For example, if the user types 5, then n = 5.

2. range(1, n + 1)
range(1, n + 1) creates a list of numbers starting from 1 up to and including n.

Example: If n = 5, this creates: 1, 2, 3, 4, 5

3. map(str, range(1, n + 1))
map(str, ...) converts each integer in the range to a string.

Example: ["1", "2", "3", "4", "5"]

4. ''.join(...)
This joins all the strings together into one long string with no space between them.

The '' means "join with an empty string".

Example: '1' + '2' + '3' + '4' + '5' = '12345'

5. print(result)
This prints the final string to the screen.

🔄 In Summary:
You're:

Getting a number from the user

Generating a list of numbers from 1 to that number

Turning those numbers into strings

Joining them all together

Printing the final string

'''
'''
The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.

Example

Print the string .

Input Format

The first line contains an integer .

Constraints


Output Format

Print the list of integers from  through  as a string, without spaces.

'''

if __name__ == '__main__':
    n = int(input())
    
result = ''.join(map(str,range(1, n + 1)))
print(result)
