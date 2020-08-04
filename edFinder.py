import click
import urllib.parse as urlparse
from urllib.parse import parse_qs
from tqdm import tqdm

@click.command()
@click.option('-f','--file')
@click.option('-o','--output')
def main(file,output):
    f=open(file,"r")
    if(output is not None):
        o=open(output,"w")
    count = len(f.readlines())
    f.seek(0)
    for line in tqdm(f,total=count):
        url=urlparse.urlparse(line)
        parameters=parse_qs(url.query)
        if(len(parameters) >0):
            if(output is not None):
                o.write(line)
            tqdm.write(line.rstrip('\n'))

    f.close()
    if(output is not None):
        o.close()
if(__name__=='__main__'):
    main()
