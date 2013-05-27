from codejam.utils.codejamrunner import CodeJamRunner
import codejam.utils.graphing as graphing
import networkx as nx

"""
Most of this algorithm is there, but it is a hideous mess, and
there are some bugs in it that with some tidying and tests should
be removed.

"""

class Dynam(object):pass

class PartialOption(object):

    def __init__(self, dic, encoded_string, count_from_last_swap, error_count=0):
        self.dic = dic
        self.encoded_str = encoded_string
        self.count_from_last_swap = count_from_last_swap
        self.error_count = error_count
        
    def next_letter(self):
        return self.encoded_str[0]

    def is_word_end(self):
        return '.' in self.dic

    def is_message_end(self):
        return not self.encoded_str
          
        
class FuzzyDict(object):

    def __init__(self, start_words):

        self.base_dict = {}
        self.max_depth = 0

        for word in start_words:
            self.add_word(word)
        
    def add_word(self, word):
        td = self.base_dict
        for i, letter in enumerate(word):
            if letter in td:
                td = td[letter]
            else:
                td[letter] = {}

        if i >= self.max_depth:
            self.max_depth = i +1

        td['.'] = '.'

    def find_options(self, encoded_str, count_from_last_swap, error_count):

        num_errors = 0 # this is a place holder and needs linking to the loop below.
        td = self.base_dict
        i=0 
        # looks like this is double iterative
        options = []
        partial_options = [PartialOption(td, encoded_str, count_from_last_swap,
                                         error_count)]
        
        while partial_options:
            po = partial_options.pop()
            
            if po.next_letter() in td:
                npo = PartialOption(td[po.next_letter()], po.encoded_str[1:],
                                    po.count_from_last_swap + 1, po.error_count)
                if '.' in td:
                    options.append(npo)

            if po.count_from_last_swap >=5:
                for letter in po.dic:
                    if letter != po.next_letter():
                        npo = PartialOption(po.dic[letter],
                                            po.encoded_str[1:], 0,
                                            po.error_count + 1)

                        if npo.is_word_end():
                            options.append(npo)
                        else:
                            npo.dic = self.base_dict
                            partial_options.append(npo)

        return options
    

class FileWrapper(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def enum_file(self):
        with open(self.file_path) as f:
            for line in f.readlines():
                yield line.strip()

file_wrapper = FileWrapper('dictionary.txt')
fuzzy_dic = FuzzyDict(file_wrapper.enum_file())

def solver(data):

    dic = fuzzy_dic    

    options = [PartialOption(dic.base_dict, data.message, 5, 0)]
    min_err = 100000

    while options:
        import pdb;pdb.set_trace()
        op = options.pop()
        new_options = dic.find_options(op.encoded_str, op.count_from_last_swap,
                                       op.error_count)
        comp_options = [op.error_count for op in new_options if op.is_message_end()]
        for sol in comp_options:
            print sol
            
        if comp_options:
            min_err  = min(min_err, min(comp_options))
        options += [op for op in new_options if not op.is_message_end()]

    if min_err == 100000:
        import pdb;pdb.set_trace()
        
    return min_err

  
def data_builder(f):

    data = Dynam()
    data.message = f.readline()

    return data



cjr = CodeJamRunner()
cjr.run(data_builder, solver, problem_name = "C")#, problem_size='small-practice')
