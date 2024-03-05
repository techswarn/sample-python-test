import pyjokes
import psycopg

import psycopg
from psycopg.sql import SQL, Identifier
from psycopg.rows import dict_row

def main(args):
  joke = pyjokes.get_joke()
  return {
    'body': {
      'response_type': 'in_channel',
      'text': joke
    }
  }
