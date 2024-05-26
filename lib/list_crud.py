def create_an_empty_list():
    return []

def create_a_list():
     new_list = ["apple", 42, True, 3.14]
     return new_list

def add_element_to_end_of_list(new_list, element):
     new_list.append(element)
     return new_list
def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    if l:
        del l[-1]
    return l

def remove_element_from_start_of_list(l):
    if l:
        del l[0]
    return l

def retrieve_first_element_from_list(l):
     if l:
        return l[0]
     else:
        return None
    

def retrieve_element_from_index(l, index):
     if 0 <= index < len(l):
        return l[index]
     else:
        return None
    

def retrieve_last_element_from_list(l):
    if l:
        return l[-1]
    else:
     return None
