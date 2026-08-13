class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inpar = ("(", "[", "{")
        out = set()
        out.add(")")
        out.add("]")
        out.add("}")

        for a in s:
            if a in inpar:
                stack.append(a)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if ord(top) + 1 != ord(a) and ord(top) +2 != ord(a):
                    return False
        return True if not stack else False