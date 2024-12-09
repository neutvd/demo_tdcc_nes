import pytest

import demo_tdcc_nes
import demo_tdcc_nes.hello

@pytest.mark.parametrize('thing, expected', [("TDCC-NES", "Hello TDCC-NES")])
def test_hello(thing: str, expected: str) -> None:
    result = demo_tdcc_nes.hello.hello(thing)
    assert result == expected