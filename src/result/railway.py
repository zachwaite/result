from functools import partial, reduce

from .result import Ok, Result


def bind(fn):
    def bound(rs) -> Result:
        if isinstance(rs, Ok):
            return fn(rs.unwrap())
        else:
            return rs
    return bound


def compose(*fns):
    return partial(reduce, lambda acc, f: f(acc), fns) 


def pipe(value, *fns):
    return compose(*fns)(value)
