import pyjokes
import psycopg

import psycopg
from psycopg.sql import SQL, Identifier
from psycopg.rows import dict_row

with psycopg.connect("dbname=defaultdb user=swarn password=AVNS_boMds5SJ8wQYoQX_4w- port=25060") as conn:

  def main(args):
    joke = pyjokes.get_joke()
    return {
      'body': {
        'response_type': 'in_channel',
        'text': joke
      }
    }
