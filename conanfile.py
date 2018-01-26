import os
from conans import ConanFile, CMake, tools

class H3DAPIWinDepsConan(ConanFile):
    name = "h3dapi_example"
    version = "0.1"
    settings = "os", "compiler"
    url = "https://github.com/ulricheck/h3dapi_example_conan"

    requires = (
        "h3dapi/2.4-beta@camposs/stable",
        "medx3d/1.5-beta@camposs/stable",
        "h3dui/2.4-beta@camposs/stable",
        "h3dphysics/1.4-beta@camposs/stable",
        )

    generators = "virtualrunenv"


    def imports(self):
        self.copy("*.exe", src="bin64", dst="bin")
        self.copy("*.dll", src="bin64", dst="bin")
        self.copy("*", src="examples", dst="examples")


