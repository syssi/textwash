import os

_BASE = os.path.dirname(os.path.abspath(__file__))

class Config:
    def __init__(self, language):
        self.path_to_months_file = os.path.join(_BASE, "data", "months.txt")
        self.path_to_written_numbers_file = os.path.join(_BASE, "data", "written_numbers.txt")

        assert language in ["nl", "en"], f"Invalid language {language} specified (only 'nl' and 'en' supported)"

        self.path_to_model = os.path.join(_BASE, "data", language)
        self.model_type = "bert" if language == "nl" else "roberta"
