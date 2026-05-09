# How to assign multipkle lne string to a variable 

'''
like, this= "Hello my name is Aditya and 
here I am learning Python and I am loving it"


But this is not the correct way to assign a multi line string to a variable, we can use triple quotes for that purpose, like this:

'''


multi_line_string = """Hello my name is Aditya and
here I am learning Python and I am loving it"""


# Now withing those triple quotes we can write as many lines as we want and it will be assigned to the variable multi_line_string without any issues.


multi_line_string2 = '''This is another way to assign a multi line string to a variable using triple single quotes.
This is also perfectly valid and works the same way as triple double quotes.
You can choose either of them based on your preference or the need to include certain types of quotes within the string.'''
### Escape Characters

# Escape characters are special characters that allow us to include characters in a string that would otherwise be difficult or impossible to include directly. They are typically represented by a backslash (\) followed by a specific character.
# For example, if we want to include a double quote within a string that is enclosed in double quotes, we can use the escape character like this:
string_with_quote = "She said, \"Hello!\""
# In this example, the backslash before the double quotes allows us to include the double quotes as part of the string without ending it prematurely.


# one more fact about py 
'''
 1. In Python, you can use triple quotes (either ''' or''') to create multi-line strings. This allows you to include line breaks and other formatting within the string without needing to use escape characters for newlines.
 2. Triple quotes are also useful for creating docstrings, which are multi-line comments that describe the purpose of a function, class, or module. Docstrings are typically enclosed in triple quotes and can be accessed using the __doc__ attribute of the object they describe.
 3. When using triple quotes for multi-line strings, the string will include all the whitespace and line breaks as they appear in the code. This means that if you have indentation or extra spaces, they will be part of the string. To avoid this, you can use the textwrap.dedent() function from the textwrap module to remove any common leading whitespace from each line in the string.
 '''



# next point
 '''
 For Loops we have one more topic to cover and that is the use of the range() function in for loops. The range() function is a built-in function in Python that generates a sequence of numbers. It can take one, two, or three arguments to specify the start, stop, and step of the sequence.
 - If you provide one argument, it will be treated as the stop value, and the sequence will start from 0. For example, range(5) will generate the numbers 0, 1, 2, 3, and 4.
 '''