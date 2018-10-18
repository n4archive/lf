#!/data/data/com.termux/files/usr/bin/python3
import lfstd
class LFError(Exception):
    pass
class Interpreter:
    def lferror(self,text):
        raise LFError(text)
    def __EvalFunc(self,dat,globaldata):
        funcname = dat[0].replace(")","")
        argv = [self.__Eval(expr,globaldata) for expr in dat[1:]]
        try:
            try:
                return lfstd.func[funcname](argv,globaldata)
            except KeyError:
                return globaldata["(lfx"][funcname](argv,globaldata)
        except KeyError as e:
            ed = str(e)
        self.lferror("FunctionNotFoundError: " + ed)
    def __Eval(self,expr:str,globaldata):
        if expr == "":
            return ""
        elif expr.startswith("//") or expr.startswith("#") or expr.startswith("(comment"):
            return ""
        elif expr[0] == "(" and expr[-1] == ")":
            results = [expr[1:].split(" ")[0],""]
            exprp = expr[2+len(results[0]):-1]
            i = 0
            appnd = 0
            while i < len(exprp):
                j = exprp[i]
                if j == "(":
                    appnd += 1
                if appnd > 0:
                    results[-1] = results[-1] + j
                if j != " " and appnd < 1:
                    results[-1] = results[-1] + j
                if j == " " and appnd < 1:
                    results.append("")
                if j == ")":
                    appnd -= 1
                i += 1
            return self.__EvalFunc(results,globaldata)
        else:
            return expr
    def __EvalAll(self,content:str,globaldata):
        for line in content.split("\n"):
            for expr in line.split(";"):
                if expr != "":
                    self.__Eval(expr,globaldata)
    def run_all(self,content:str,globaldata:dict={"(lfx":{}}):
        self.__EvalAll(content,globaldata)
def run_file(file:str):
    with open(file,"r") as _FileInput:
        _FileInputContent = _FileInput.read()
        Interpreter().run_all(_FileInputContent)
