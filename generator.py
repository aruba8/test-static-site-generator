from jinja2 import Environment, PackageLoader
import uuid

env = Environment(loader=PackageLoader('generator', 'templates'))
template = env.get_template('template.html')



if __name__ == '__main__':
    uuid_list = [uuid.uuid1() for x in range(200)]
    for x in range(len(uuid_list)):
        if (x+2)<len(uuid_list):
            with open(str(uuid_list[x+1])+'.html', 'w') as fh:
                fh.write(template.render(prev=str(uuid_list[x]), curr=str(uuid_list[x+1]), next=str(uuid_list[x+2])))
