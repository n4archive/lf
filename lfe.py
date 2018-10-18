import liblf
def tf(argv,globaldata):
    print("Halohl World per globaldata?!")
liblf.Interpreter().run_all("""
#lf :)
(test)
#py :)
""",{"(lfx":{"test":tf}})
