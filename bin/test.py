from rich.table import Table
from rich.console import Console
import flatdict

console = Console()


def dict_to_rich_table(data: dict, table: Table=None):
    if table is None:
        table = Table('Dict View By Rich Table', show_lines=True)

    flatted_dict = flatdict.FlatDict(data)
    for k, v in flatted_dict.items():
        table.add_row(k, f'{v}')

    return table

data = {'init_done': True,
 'timezone': 'Asia/Chongqing',
 'docker_unix_sock': 'unix:///var/run/docker.sock',
 'raw_config_info': {'core_database': {'connect_string': 'sqlite+aiosqlite:////Users/liufeng/CodeHome/sandcloudhub/pearl/pearl_core/pearl.db',
   'pool_size': 4},
  'docker_unix_sock': 'unix:///var/run/docker.sock',
  'http_server': {'host': '0.0.0.0', 'port': 45678},
  'sandbank': {'host': 'xxx.sandbank.com',
   'pearl_id': 'pppeeeaaarllllid',
   'protocols': [{'protocol': 'https', 'version': 'v1'}]},
  'secret_key': 'some_str',
  'storages': [{'access_key': 'lxQSOYdq3UTIWanYDXnx_raoiaLzlSbkrwUYnD7M',
    'access_key_secret': '8OZfuVvrAyaBq7QHIJGy7-tGceYL5AO7rRf_nx93',
    'bucket': 'anywhere-private',
    'dialect': 'qiniu',
    'driver': 'pal_qiniu',
    'max_can_use': 100,
    'inside_endpoint': 'http://static.qnpri.crazytech.cn',
    'outside_endpoint': 'http://static.qnpri.crazytech.cn',
    'region': 'NCN',
    'root_path': 'paltest/'}],
  'timezone': 'Asia/Chongqing'},
 'http_server': {'host': '0.0.0.0', 'port': 45678},
 'core_database': {'connect_string': 'sqlite+aiosqlite:////Users/liufeng/CodeHome/sandcloudhub/pearl/pearl_core/pearl.db',
  'pool_size': 4},
 'storages': [{'access_key': 'lxQSOYdq3UTIWanYDXnx_raoiaLzlSbkrwUYnD7M',
   'access_key_secret': '8OZfuVvrAyaBq7QHIJGy7-tGceYL5AO7rRf_nx93',
   'bucket': 'anywhere-private',
   'dialect': 'qiniu',
   'driver': 'pal_qiniu',
   'max_can_use': 100,
   'inside_endpoint': 'http://static.qnpri.crazytech.cn',
   'outside_endpoint': 'http://static.qnpri.crazytech.cn',
   'region': 'NCN',
   'root_path': 'paltest/'}],
 'storage_schemas': [{'dialect': 'qiniu',
   'driver': 'pal_qiniu',
   'root_path': 'paltest/',
   'max_can_use': 100,
   'bucket': 'anywhere-private',
   'access_key': 'lxQSOYdq3UTIWanYDXnx_raoiaLzlSbkrwUYnD7M',
   'access_key_secret': '8OZfuVvrAyaBq7QHIJGy7-tGceYL5AO7rRf_nx93',
   'inside_endpoint': 'http://static.qnpri.crazytech.cn',
   'outside_endpoint': 'http://static.qnpri.crazytech.cn',
   'region': 'NCN'}],
 'storage_schemas_map': {'qiniu:anywhere-private': {'dialect': 'qiniu',
   'driver': 'pal_qiniu',
   'root_path': 'paltest/',
   'max_can_use': 100,
   'bucket': 'anywhere-private',
   'access_key': 'lxQSOYdq3UTIWanYDXnx_raoiaLzlSbkrwUYnD7M',
   'access_key_secret': '8OZfuVvrAyaBq7QHIJGy7-tGceYL5AO7rRf_nx93',
   'inside_endpoint': 'http://static.qnpri.crazytech.cn',
   'outside_endpoint': 'http://static.qnpri.crazytech.cn',
   'region': 'NCN'}},
 'sandbank': {'host': 'xxx.sandbank.com',
  'pearl_id': 'pppeeeaaarllllid',
  'protocols': [{'protocol': 'https', 'version': 'v1'}]},
 'secret_key': 'some_str'}


t = dict_to_rich_table(data)

console.print(t)
