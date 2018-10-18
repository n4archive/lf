def _Print(argv,globaldata):
    print(" ".join(argv))

def echo(argv,globaldata):
    return " ".join(argv)

def _Comment(argv,globaldata):
    return ""

def setvar(argv,globaldata):
    globaldata[argv[0]] = " ".join(argv[1:])

def getvar(argv,globaldata):
    return globaldata[argv[0]]

def lfx(argv,globaldata):
    import importlib
    lfxtmp=importlib.import_module(argv[0])
    if lfxtmp.lfx:
        def lfxregf(name,run):
            globaldata["(lfx"][name] = run
        lfxtmp.lfx({"register_func":lfxregf})

# __func

func = {
        "print":_Print,
        "echo":echo,
        "comment":_Comment,
        "setvar":setvar,
        "getvar":getvar,
        "lfx":lfx
}
