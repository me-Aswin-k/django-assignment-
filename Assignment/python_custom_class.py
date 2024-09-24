class Rectangle:

    def __init__(self, length: int, width: int):

        self.length = length

        self.width = width

         
    # Make the Rectangle class iterable
    def __iter__(self):

        # Create a list of tuples that match the required format
        self._attributes = [{'length': self.length}, {'width': self.width}]

        self._index = 0 

        return self
    
    # Define the method to handle iteration
    def __next__(self):

        if self._index < len(self._attributes):

            result = self._attributes[self._index]

            self._index += 1

            return result
        
        else:

            raise StopIteration 

