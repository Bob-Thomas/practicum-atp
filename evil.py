import re
class SimpleSecureEvaluator(object):
    d = {} # empty dictionary
    def __init__(self):
        # TODO
        pass

    def eval(self, expressie):
        if expressie == 'mydir':
            self.my_dir()
            return

        l = expressie.strip().split(' ')
        variable = l[0]
        variable = self.assign(variable, l[2::])

        return expressie

    def my_dir(self):
        [print('%s : %s' % (k, v)) for k,v in self.d.items()]

    def assign(self, var, l):
        for item in l:
            if item in self.d.keys():
                l[l.index(item)] = str(self.d[item])
            if not re.match('^(\w+|\d|\+|\*|\-|\^)$', item):
                print("not allowed: ", ' '.join(l))
                return
        self.d[var] = eval(' '.join(l))

s = SimpleSecureEvaluator()
s.eval('v = 1')
s.eval('v = print(\'bad stuff\')')
s.eval('v = 1 + 1 + 1 + 1')
s.eval('davde = v + 20')
s.eval('geen_dave = davde')
s.eval('i = 1+4[eval\u0028\"print\u0028\\\"hi\\\"\u0029\u0029] +  2')
s.eval('i = 1+2')
s.eval('mydir')