my_string = "Hello, World!"

# Print the length of my_string
print(len(my_string))

# Print "World" from my_string
print(my_string[7:-1])

# Print charcter "H" from my_string
print(my_string[0])

# Print "HELLO, WORLD!" from my_string
print(my_string.upper())

# Print "hello, world!" from my_string
print(my_string.lower())

# Print "Bye Bye, World!" from my_string
print(my_string.replace("Hello", "Bye Bye"))

# Print a splitted my_string, split at ","
print(my_string.split(","))

# Print "This is my world, say "Hello, World!"" (using Concatenation and Escape Character)
print("This is my world, say \"" + my_string +"\"")


student_name = "Not a real student name"
grade = 12

# Print "my name is Not a real student name from grade 12" using fotmat string
print(f"my name is {student_name} from grade {grade}")
