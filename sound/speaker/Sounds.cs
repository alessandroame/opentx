using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace OpenTXspeaker
{
    public class SoundsDefinition
    {
        public Sound[] SystemSounds { get; set; }
        public Sound[] OtherSounds { get; set; }
    }
    public class Sound
    {
        public string Id { get; set; }
        public string Speech { get; set; }
    }
}
