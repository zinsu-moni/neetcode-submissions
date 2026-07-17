class Solution:

    def encode(self, strs):
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded


    def decode(self, encoded_string):
        result = []

        i = 0

        while i < len(encoded_string):

            # find #
            j = i

            while encoded_string[j] != "#":
                j += 1

            # get length
            length = int(encoded_string[i:j])

            # move after #
            j += 1

            # get the string
            word = encoded_string[j:j+length]

            result.append(word)

            # move pointer
            i = j + length

        return result