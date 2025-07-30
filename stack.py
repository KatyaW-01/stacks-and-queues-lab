def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # TODO: Implement stack logic to validate parentheses
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        #if the last character in the string makes it a valid parentheses, remove it 
        elif len(stack) > 0 and char == ')' and stack[-1] == '(':
            stack.pop()
        elif char == '{':
            stack.append(char)
        elif len(stack) > 0 and char == '}' and stack[-1] == '{':
            stack.pop()
        elif char == '[':
            stack.append(char)
        elif len(stack) > 0 and char == ']' and stack[-1] == '[':
            stack.pop()

    #if the list is empty it means all the parentheses were valid because they were all removed
    if len(stack) == 0:
        return True
    else:
        False

