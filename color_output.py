#coding:utf-8
'''实现windows cmd下的彩色输出（通过pyreadline），并对编码转换进行了包装
by Kder [ http://www.kder.info/ ]
'''
import sys
import rlcompleter

def uprint(msg):
    msg = str(msg)
    try:
        print(msg.decode('utf-8'))
    except UnicodeDecodeError as e:
        print(msg.decode('gbk'))

if sys.platform == 'win32':
    try:
        import pyreadline
        pyreadline.parse_and_bind("tab: complete")
        sys.stdout = pyreadline.console.Console(0)
    except:
        pass
    # colored = colored_console.write_color
else:
    import readline
    readline.parse_and_bind("tab: complete")


if __name__ == "__main__":
    uprint("\033[32m绿色\033[0m　\033[36m蓝色\033[0m　\033[31m红色\033[0m")
