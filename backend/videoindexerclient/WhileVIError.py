class WhileIndexingError(Exception):
    """
    Exception raised while polling for indexing status
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class WhileGeneratingPromptError(Exception):
    """
    Exception raised while polling for prompt generation status
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)