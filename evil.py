import re

from notebook.notebookapp import raw_input


class SimpleSecureEvaluator(object):
    d = {} # empty dictionary
    def __init__(self, d={}):
        # TODO
        self.d = d

    def eval(self, expressie):
        eList = re.sub('(\(|\)|[+\-*\^\/=])', ' \\1 ', expressie).split()
        if expressie == 'mydir':
            [print("%s : %s" % (k, v)) for (k, v) in self.d.items()]
            return
        if len(eList) == 1 and eList[0] in self.d:
            print('%s = %s' % (eList[0], self.d[eList[0]]))
            return
        elif len(eList) == 1 and eList[0] not in self.d:
            print("invalid expression")
            print("valid expressions are")
            [print("%s : %s" % (k, v)) for (k, v) in self.d.items()]
            print("variable = math expression")
            return

        if eList[1] == '=':
            self.assign(eList[0], eList[2::])

    def assign(self, var, expr):
        for char in list(expr):
            if not re.match('(\w|\(|\)|[+\-*\^\/])', char):
                return
        for key in self.d.keys():
            if key in expr:
                expr = ' '.join(expr).replace(key, str(self.d[key])).split(' ')
        for word in expr:
            if re.match('[a-zA-Z]', word):
                if word not in self.d.keys():
                    print('%s not defined' % word)
                    return
        result = eval(''.join(expr))
        self.d[var] = result



s = SimpleSecureEvaluator()
s.eval('a=1')
s.eval('b = a')
s.eval('c = a + b')
s.eval('nee = nope + 3')
s.eval('nee = 2')
s.eval('mydir')

while True:
    d = input()
    s.eval(d)
