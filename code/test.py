class test():
    def __init__(self, **kargs):
        print('init')
        self.a = 'atri1'

    def __call__(self, x):
        print('call')
        self.met1(x)

    def met1(self, b):
        print('met1')
        at= b
        print(at[0])

t = test()(['a'])

