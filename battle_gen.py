import json
import random


class PersonNameGen():
    def __init__(self):
        self.json_path = "./宋词三百首.json"
        self.not_desired_chars = ["", "，", "。", "；", "、", "", "", "", "", "", "", ""]
        self.family_names = []
        with open("./family_names_clear.txt",'r',encoding='utf8') as file:
                names = file.readlines()
                # print(type(names))
                for name in names:
                    self.family_names.append(name[:-1])
        # print(self.family_names)

    def generate_person_name(self):
        with open(self.json_path, 'r', encoding='utf8') as ci:
            json_data = json.load(ci)
            # print(json_data[0]['paragraphs'])
            # print(type(json_data[0]['paragraphs']))
            choice = random.choice(json_data)['paragraphs']
            # print(choice)
            choice_clear = []
            for juzi in choice:
                for char in juzi:
                    if char not in self.not_desired_chars:
                        choice_clear.append(char)
            # print(choice_clear)
            # print(type(choice))
            chosen_name = ""
            for i in range(2):
                chosen_name += random.choice(random.choice(choice_clear))
            # print(chosen_name)
            return chosen_name
    
    def generate_full_name(self):
        given_name = self.generate_person_name()
        family_name = random.choice(self.family_names)
        full_name = family_name + given_name
        return full_name


if __name__ == "__main__":
    person_name_gen = PersonNameGen()
    person_names = []
    for i in range(10):
        person_names.append(person_name_gen.generate_full_name())
    print(person_names)
