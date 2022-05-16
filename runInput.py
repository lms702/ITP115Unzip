from subprocess import run


def runA4(path):
    cmd = f'python {path} < runA4.txt'
    print(cmd)
    run(cmd, shell=True)




# runA4("a4_ballatore_anna.py/a4_ballatore_anna.py")