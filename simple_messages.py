import sys

message = "Hello, Python!"
print(message)
message = "Hello again, Python!"
print(message)
message = "This is an error message now!"
print(message, file=sys.stderr)

