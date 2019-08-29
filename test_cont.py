import pytest
from mdtoc import mdtoc


@pytest.mark.parametrize(
    'arg',
    [
        ('name: someslide\n# Foo'.split('\n'), '* [Foo](#someslide)\n'),
        ('name: someslide\n## Foo'.split('\n'), '    + [Foo](#someslide)\n'),
        ('name: someslide\n### Foo'.split('\n'), '        - [Foo](#someslide)\n'),
        ('name: someslide\n#### Foo'.split('\n'), '            ^ [Foo](#someslide)\n'),
        (

'''
name: first
# foo

name: second
## bar
'''.split('\n')
,

'''\
* [foo](#first)
    + [bar](#second)
'''
        ),
    ],
)
def test_foo(arg):
    src, expected = arg

    toc = mdtoc(src)
    assert toc == expected
